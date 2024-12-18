class NotificationManager {
    static async initialize() {
        if (!('Notification' in window)) {
            console.log('This browser does not support notifications');
            return;
        }

        if (Notification.permission === 'default') {
            await Notification.requestPermission();
        }

        if (Notification.permission === 'granted') {
            await this.registerServiceWorker();
        }
    }

    static async registerServiceWorker() {
        try {
            const registration = await navigator.serviceWorker.register('/static/js/notification-worker.js');
            console.log('ServiceWorker registration successful');
            return registration;
        } catch (err) {
            console.log('ServiceWorker registration failed: ', err);
        }
    }
}