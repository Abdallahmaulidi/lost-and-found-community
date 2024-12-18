self.addEventListener('push', function(event) {
    const data = event.data.json();
    
    const options = {
        body: data.message,
        icon: '/static/img/notification-icon.png',
        badge: '/static/img/notification-badge.png',
        data: {
            url: data.url
        }
    };

    event.waitUntil(
        self.registration.showNotification('Lost and Found', options)
    );
});

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    event.waitUntil(
        clients.openWindow(event.notification.data.url)
    );
});