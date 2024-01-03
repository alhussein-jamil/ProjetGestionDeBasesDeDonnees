import sys
from collections import defaultdict
import seaborn as sns  
import matplotlib
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget,
                             QVBoxLayout, QWidget)

matplotlib.use("qt5agg")
FIG_SIZE = (10, 10)

# Replace these with your MySQL database credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "user4projet",
    "password": "Hellogenielogiciel2023",
    "database": "accidentsroutiers",
    "auth_plugin": "mysql_native_password",
}
# DB_CONFIG = {
#     "host": "localhost",
#     "user": "CyberTitan",
#     "password": "19216811",
#     "database": "accidentsroutiers",
# }

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)


# Function to execute a query and return a DataFrame
def execute_query(query, connection):
    df = pd.read_sql_query(query, connection)
    return df

class PlotWindow:
    def __init__(self, parent=None):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.MainWindow.__init__()
        self.MainWindow.setWindowTitle("plot window")
        self.canvases = []
        self.figure_handles = []
        self.toolbar_handles = []
        self.tab_handles = []
        self.current_window = -1
        self.tabs = QTabWidget()
        self.MainWindow.setCentralWidget(self.tabs)
        self.MainWindow.resize(1280, 900)
        self.MainWindow.show()

    def addPlot(self, title, figure):
        figure.tight_layout(rect=[0, 0, 1, 1])  # Adjust layout for the entire figure
        new_tab = QWidget()
        layout = QVBoxLayout()
        new_tab.setLayout(layout)

        figure.subplots_adjust(
            left=0.1, right=0.95, bottom=0.3, top=0.9, wspace=0.2, hspace=0.2
        )
        new_canvas = FigureCanvas(figure)
        new_toolbar = NavigationToolbar(new_canvas, new_tab)

        layout.addWidget(new_canvas)
        layout.addWidget(new_toolbar)
        self.tabs.addTab(new_tab, title)

        self.toolbar_handles.append(new_toolbar)
        self.canvases.append(new_canvas)
        self.figure_handles.append(figure)
        self.tab_handles.append(new_tab)

    def show(self):
        self.app.exec_()


def plot3d(
    df: pd.DataFrame,
    x: str,
    y: str,
    z: str,
    t: str,
    title: str,
    x_label: str,
    y_label: str,
    z_label: str,
    x_continuous: bool = True,
    y_continuous: bool = True,
    z_continuous: bool = True,
    t_continuous: bool = True,
):
    if not x_continuous:
        df[x] = pd.Categorical(df[x])
    else:
        # make into buckets
        df[x] = pd.cut(df[x], 10)
        df[x] = pd.Categorical(df[x])

    if not y_continuous:
        df[y] = pd.Categorical(df[y])
    else:
        # make into buckets
        df[y] = pd.cut(df[y], 10)
        df[y] = pd.Categorical(df[y])

    if not z_continuous:
        df[z] = pd.Categorical(df[z])
    else:
        # make into buckets
        df[z] = pd.cut(df[z], 10)
        df[z] = pd.Categorical(df[z])

    if not t_continuous:
        df[t] = pd.Categorical(df[t])
    else:
        # make into buckets
        df[t] = pd.cut(df[t], 10)
        df[t] = pd.Categorical(df[t])

    # the one or two variables that are not continuous are categorical
    # the two categorical variables are plotted on the x and y axis
    # and the continuous variable is plotted as the height of the bars
    # transform the categorical variables to numerical representations
    x_categories = list(df[x].cat.categories)
    y_categories = list(df[y].cat.categories)
    t_categories = list(df[t].cat.categories)

    df[z] = df[z].cat.codes if df[z].dtype == "category" else df[z]
    df[x] = df[x].cat.codes if df[x].dtype == "category" else df[x]
    df[y] = df[y].cat.codes if df[y].dtype == "category" else df[y]
    df[t] = df[t].cat.codes if df[t].dtype == "category" else df[t]

    # Combine z values for duplicate (x, y) pairs
    data_dict = {}
    for _, row in df.iterrows():
        if row[t] not in data_dict:
            data_dict[row[t]] = defaultdict(int)
        data_dict[row[t]][(row[x], row[y])] += row[z]

    # Create a 3D axis
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111, projection="3d")

    # Use bar3d to create 3D bars
    colors = [
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "yellow",
        "pink",
        "black",
        "brown",
        "gray",
    ]
    offsets = {}
    for i, ti in enumerate(data_dict.keys()):
        x_combined, y_combined = zip(*data_dict[ti].keys())
        z_combined = list(data_dict[ti].values())
        local_offset = [offsets.get((x, y), 0) for x, y in zip(x_combined, y_combined)]
        ax.bar3d(
            x_combined,
            y_combined,
            local_offset,
            0.8,
            0.8,
            z_combined,
            shade=True,
            color=colors[i % len(colors)],
            alpha=1,
        )
        offsets.update(
            {
                (x, y): z + offset
                for x, y, z, offset in zip(
                    x_combined, y_combined, z_combined, local_offset
                )
            }
        )

    # Set labels for the axes
    ax.set_xlabel(x_label, ha="right")
    ax.set_ylabel(y_label, ha="left")
    ax.set_zlabel(z_label)

    # Set tick labels for x and y axes
    ax.set_xticks(range(len(x_categories)))
    ax.set_xticklabels(x_categories, rotation=90, fontsize=8)

    ax.set_yticks(range(len(y_categories)))
    ax.set_yticklabels(y_categories, rotation=90, fontsize=8)

    ax.set_title(title)
    ax.legend(t_categories)
    return fig

def plot2D(df_query, x, y, z, title, scat, pie):
    figure = None  # Initialiser la variable figure

    if scat:
        z_mapping = {"Indemne": 1, "Blessé léger": 2, "Blessé hospitalisé": 3, "Tué": 4}
        df_query["Severity"] = df_query[z].map(z_mapping)

        figure, ax = plt.subplots(figsize=FIG_SIZE)

        # Use Seaborn color palette
        scatter = ax.scatter(
            df_query[x], df_query[y], c=df_query["Severity"], cmap="viridis", s=100
        )

        # Ajout de la barre de couleur avec les noms de gravité
        cbar = plt.colorbar(scatter, ax=ax, ticks=list(z_mapping.values()))
        cbar.set_ticklabels(list(z_mapping.keys()), rotation=30, fontsize=10)
        cbar.set_label("Severity")

        # Ajout des labels et du titre
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(title)

    elif pie:
        # Use Seaborn color palette
        sns.set_palette("pastel")
        
        # Pie chart
        figure, ax = plt.subplots(figsize=FIG_SIZE)
        ax.pie(df_query[y], labels=df_query[x], autopct="%1.1f%%", startangle=140)
        ax.set_title(title)

    elif title == "Manoeuvre Types and Accident Outcomes":
        figure, ax = plt.subplots(figsize=FIG_SIZE)

        # Use Seaborn color palette
        sns.set_palette("pastel")
        
        # Bar chart
        bar_width = 0.6
        bar_positions = range(len(df_query["Manoeuvre"]))

        # Bar pour les accidents mortels
        ax.bar(
            bar_positions,
            df_query["Death Accidents"],
            width=bar_width,
            label="Death Accidents",
        )

        # Bar pour les accidents avec blessures graves
        ax.bar(
            bar_positions,
            df_query["Serious Injury Accidents"],
            bottom=df_query["Death Accidents"],
            width=bar_width,
            label="Serious Injury Accidents",
        )

        # Bar pour les accidents sans blessure
        ax.bar(
            bar_positions,
            df_query["Unscathed Accidents"],
            bottom=df_query["Death Accidents"] + df_query["Serious Injury Accidents"],
            width=bar_width,
            label="Unscathed Accidents",
        )

        # Configurations d'axe et de titre
        ax.set_xticks(bar_positions)
        ax.set_xticklabels(df_query["Manoeuvre"], rotation=30, ha="right", fontsize=10)
        ax.set_xlabel("Manoeuvre Types")
        ax.set_ylabel("Number of Accidents")
        ax.set_title(title)
        ax.legend()

    else:
        # Use Seaborn color palette
        sns.set_palette("pastel")
        
        # Bar chart
        figure, ax = plt.subplots(figsize=FIG_SIZE)
        ax.bar(df_query[x], df_query[y])
        ax.set_xticklabels(df_query[x], rotation=30, ha="right")

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(title)

    return figure


def plot_query(df_query, title, plot_3D, scatter, pie):
    if plot_3D:
        # add an artifical column if len(columns) < 4
        if len(df_query.columns) < 4:
            df_query["artificial"] = 0
        columns = df_query.columns
        return plot3d(
            df_query, *columns[:4], title, *columns[:3], False, False, False, False
        )
    else:
        columns = df_query.columns

        return plot2D(
            df_query,
            *columns[:2],
            title=title,
            scat=scatter,
            z=None if len(columns) < 3 else columns[2],
            pie=pie
        )


def plot_queries(df_queries, titles, Plot_3D, scatter, pies):
    figs = []
    pw = PlotWindow()
    for df_query, title, plot_3D, scat, pie in zip(
        df_queries, titles, Plot_3D, scatter, pies
    ):
        figs.append(plot_query(df_query, title, plot_3D, scat, pie))
        pw.addPlot(title, figs[-1])

    pw.show()


if __name__ == "__main__":
    queries = [""]
    titles = []
    plot_3D = []
    scatter = []
    figs = []
    pie = []
    df_queries = []

    # ignore comments starting with -- and each query starts with SELECT and ends with ; annd can be on multiple lines
    with open("Queries.sql") as f:
        i = 0
        for line in f:
            if "--" in line or "USE" in line:
                if "title" in line:
                    titles.append(
                        line.split("title")[1].split("=")[1].strip().replace("'", "")
                    )
                    print(titles[-1])
                else:
                    if "Query" in line:
                        if "3D" in line:
                            plot_3D.append(True)
                        else:
                            plot_3D.append(False)
                        if "scatter" in line:
                            scatter.append(True)
                        else:
                            scatter.append(False)
                        if "pie" in line:
                            pie.append(True)
                        else:
                            pie.append(False)
                continue
            queries[i] += line
            if line.endswith(";\n"):
                i += 1
                queries.append("")
    # remove last empty query
    queries.pop()

    connection = connect_to_db()

    plot_queries(
        [execute_query(query, connection) for query in queries],
        titles,
        plot_3D,
        scatter,
        pie,
    )
