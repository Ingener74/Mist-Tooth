#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from loguru import logger

@logger.catch
def main():
    import sys
    from PySide2.QtCore import QDir, QUrl
    from PySide2.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu
    from PySide2.QtGui import QPixmap, QDesktopServices, QIcon, QScreen
    
    from MainWidget import MainWidget
    from SettingsWidget import SettingsWidget
    from NotificationWidget import NotificationWidget
    from ItemWidget import ItemWidget
    from settings import settings, DOWNLOAD_DIR
    from Notifications import Notification

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    for screen in app.screens():
        logger.debug(screen.geometry())

    # iw = ItemWidget(None)
    # iw.show()
    # iw.set_thumbnail('path to image')

    main_widget = MainWidget()
    settings_widget = SettingsWidget()
    notification_widget = NotificationWidget()

    app.aboutToQuit.connect(main_widget.on_close)

    show_window_action = QAction(QPixmap(':/main/icon.png'), 'Показать Youtube Downloader')
    def show_main_window():
        main_widget.show()
        main_widget.raise_()
        main_widget.activateWindow()
    show_window_action.triggered.connect(show_main_window)

    open_download_dir_action = QAction(QPixmap(':/main/open_dir.png'), 'Открыть каталог загрузки')
    def open_download_dir():
        s = settings()
        dir = s.value(DOWNLOAD_DIR) if s.contains(DOWNLOAD_DIR) else QDir.currentPath()
        dir = f'file:///{dir}'
        QDesktopServices.openUrl(QUrl(dir))
    open_download_dir_action.triggered.connect(open_download_dir)
    
    close_action = QAction(QPixmap(':/main/close.png'), 'Выключить')
    close_action.triggered.connect(app.quit)

    tray_menu = QMenu()
    tray_menu.addAction(show_window_action)
    tray_menu.addAction(open_download_dir_action)
    tray_menu.addSeparator()
    tray_menu.addAction(close_action)

    system_tray = QSystemTrayIcon(main_widget, QPixmap(':/main/icon.png'))
    system_tray.setContextMenu(tray_menu)

    def show_complete(title, thumbnail):
        notification.show_notification('Закончено скачивание', title)

    def show_start_download(link):
        notification.show_notification('Начинается скачивание', link)

    main_widget.ui.pushButtonSettings.clicked.connect(settings_widget.show)
    main_widget.ui.pushButtonOpenDownloadDir.clicked.connect(open_download_dir)
    main_widget.start_download_signal.connect(show_start_download)
    main_widget.complete_download_signal.connect(show_complete)
    settings_widget.ui.pushButtonOpenDownloadDir.clicked.connect(open_download_dir)

    main_widget.show()
    system_tray.show()

    notification = Notification(system_tray)

    # notification.show_notification('Youtube', 'Foo')

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
