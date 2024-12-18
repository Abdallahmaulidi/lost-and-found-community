class NotificationSound {
    static async play() {
        try {
            const audio = new Audio('/static/sounds/notification.mp3');
            await audio.play();
        } catch (error) {
            console.error('Error playing notification sound:', error);
        }
    }
} 