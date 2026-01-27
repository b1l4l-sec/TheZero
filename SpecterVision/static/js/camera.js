class CameraManager {
    constructor() {
        this.video = null;
        this.canvas = null;
        this.ctx = null;
        this.stream = null;
        this.isActive = false;
        this.fps = 0;
        this.lastFrameTime = 0;
        this.frameCount = 0;
        this.emotionFrameCount = 0;
    }

    async initialize() {
        this.canvas = document.getElementById('videoCanvas');
        this.ctx = this.canvas.getContext('2d');

        this.video = document.createElement('video');
        this.video.setAttribute('autoplay', '');
        this.video.setAttribute('playsinline', '');

        try {
            this.stream = await navigator.mediaDevices.getUserMedia({
                video: {
                    width: { ideal: 640 },
                    height: { ideal: 480 }
                },
                audio: false
            });

            this.video.srcObject = this.stream;
            this.isActive = true;

            this.video.addEventListener('loadedmetadata', () => {
                this.canvas.width = this.video.videoWidth;
                this.canvas.height = this.video.videoHeight;
                this.render();
            });

            return true;
        } catch (error) {
            console.error('Camera access denied:', error);
            alert('Camera access denied. Please allow camera permissions and try again.');
            return false;
        }
    }

    render() {
        if (!this.isActive) return;

        this.ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);

        this.calculateFPS();

        if (window.emotionDetector && window.emotionDetector.isEnabled) {
            this.emotionFrameCount++;
            if (this.emotionFrameCount % 2 === 0) {
                window.emotionDetector.detect(this.canvas, this.ctx);
            }
        }

        if (window.motionDetector && window.motionDetector.isEnabled) {
            window.motionDetector.detect(this.canvas, this.ctx);
        }

        if (window.captureManager) {
            window.captureManager.updateDetectionResults();
        }

        requestAnimationFrame(() => this.render());
    }

    calculateFPS() {
        const now = performance.now();
        this.frameCount++;

        if (now - this.lastFrameTime >= 1000) {
            this.fps = this.frameCount;
            this.frameCount = 0;
            this.lastFrameTime = now;

            const fpsCounter = document.getElementById('fpsCounter');
            if (fpsCounter) {
                fpsCounter.textContent = `${this.fps} FPS`;
            }
        }
    }

    captureFrame() {
        if (!this.isActive) return null;
        return this.canvas.toDataURL('image/jpeg', 0.85);
    }

    stop() {
        this.isActive = false;

        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
            this.stream = null;
        }

        if (this.video) {
            this.video.srcObject = null;
        }

        if (this.ctx) {
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }
    }
}

window.cameraManager = new CameraManager();
