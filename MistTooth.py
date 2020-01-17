#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    from MainWidget import MainWidget
    from SettingsWidget import SettingsWidget
    
    app = QApplication(sys.argv)

    main_widget = MainWidget()
    settings_widget = SettingsWidget()

    main_widget.ui.pushButtonSettings.clicked.connect(settings_widget.show)

    main_widget.show()

    sys.exit(app.exec_())
