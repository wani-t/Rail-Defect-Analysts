from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QStackedWidget
)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QScatterSeries
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set main window properties
        self.setWindowTitle("Railway Track Monitoring GUI")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #121212; color: white;")  # Dark theme

        # Create main layout
        main_layout = QVBoxLayout()

        # Add header section
        header_layout = QHBoxLayout()

        self.location_label = self.create_label("Location: 10.123, 20.456")
        header_layout.addWidget(self.location_label)

        self.timestamp_label = self.create_label("Timestamp: 2024-11-21 12:34:56")
        header_layout.addWidget(self.timestamp_label)

        self.rail_label = self.create_label("Rail: RH")
        header_layout.addWidget(self.rail_label)

        self.rail_type_label = self.create_label("Rail Type: r62")
        header_layout.addWidget(self.rail_type_label)

        self.probe_label = self.create_label("Probe Degree: 70°")
        header_layout.addWidget(self.probe_label)

        main_layout.addLayout(header_layout)

        # Create pages (A-scan and B-scan)
        self.stacked_widget = QStackedWidget()

        # Page 1: A-scan graph
        self.page1 = self.create_a_scan_page()
        self.stacked_widget.addWidget(self.page1)

        # Page 2: B-scan graph
        self.page2 = self.create_b_scan_page()
        self.stacked_widget.addWidget(self.page2)

        main_layout.addWidget(self.stacked_widget)

        # Add navigation buttons
        button_layout = QHBoxLayout()
        self.page_indicator = QLabel("Current Page: A-Scan")
        self.page_indicator.setStyleSheet("font-size: 16px; color: yellow;")

        self.page1_button = QPushButton("A-Scan")
        self.page1_button.setStyleSheet("background-color: #1e88e5; color: white; padding: 10px; font-weight: bold;")
        self.page1_button.clicked.connect(lambda: self.show_page(self.page1, "A-Scan"))

        self.page2_button = QPushButton("B-Scan")
        self.page2_button.setStyleSheet("background-color: #43a047; color: white; padding: 10px; font-weight: bold;")
        self.page2_button.clicked.connect(lambda: self.show_page(self.page2, "B-Scan"))

        button_layout.addWidget(self.page1_button)
        button_layout.addWidget(self.page2_button)
        button_layout.addWidget(self.page_indicator)

        main_layout.addLayout(button_layout)

        # Set the main layout to the central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_label(self, text):
        """Create styled label for the header."""
        label = QLabel(text)
        label.setStyleSheet("border: 1px solid white; padding: 5px; background-color: #212121; font-size: 14px; color: lightblue;")
        return label

    def show_page(self, page, page_name):
        """Switch to the selected page and update the indicator."""
        self.stacked_widget.setCurrentWidget(page)
        self.page_indicator.setText(f"Current Page: {page_name}")

    def create_a_scan_page(self):
        """Create the A-scan graph page."""
        page = QWidget()
        layout = QVBoxLayout()

        # Create the A-scan graph
        chart = QChart()
        chart.setTitle("A-Scan: Voltage Amplitude vs Time")
        chart.setTitleBrush(QColor("white"))
        chart.setBackgroundBrush(QColor("#121212"))
        chart.legend().setVisible(False)

        # Enable grid lines for A-Scan
        series = QLineSeries()  # Continuous line series

        # Add dummy data for A-scan (replace with DB data fetching logic)
        for i in range(100):
            series.append(i, random.uniform(0, 10))

        chart.addSeries(series)
        chart.createDefaultAxes()

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(chart_view)
        page.setLayout(layout)
        return page

    def create_b_scan_page(self):
        """Create the B-scan graph page."""
        page = QWidget()
        layout = QVBoxLayout()

        # Create the B-scan graph
        chart = QChart()
        chart.setTitle("B-Scan: Fault Position in Rail Head")
        chart.setTitleBrush(QColor("white"))
        chart.setBackgroundBrush(QColor("#121212"))
        chart.legend().setVisible(False)

        series = QScatterSeries()
        series.setMarkerSize(10)
        series.setColor(QColor("red"))

        # Add dummy data for B-scan (replace with ML model output)
        for i in range(20):  # Only plot discrete points
            series.append(random.uniform(0, 100), random.uniform(0, 5))

        chart.addSeries(series)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(chart_view)
        page.setLayout(layout)
        return page


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
