class CaptureManager {
    constructor() {
        this.sessionId = null;
        this.frameCounter = 0;
        this.captureInterval = null;
        this.isCapturing = false;
        this.currentMode = 'none';
    }

    generateSessionId() {
        const now = new Date();
        const dateStr = now.toISOString().replace(/[-:]/g, '').split('.')[0].replace('T', '_');
        const random = Math.random().toString(36).substring(2, 7).toUpperCase();
        this.sessionId = `client_${dateStr}_${random}`;
        return this.sessionId;
    }

    startCapture() {
        if (this.isCapturing) return;

        this.generateSessionId();
        this.isCapturing = true;
        this.frameCounter = 0;

        document.getElementById('sessionId').textContent = this.sessionId;
        document.getElementById('statusIndicator').textContent = 'Active';
        document.getElementById('statusIndicator').className = 'info-value status-active';

        this.captureInterval = setInterval(() => {
            this.captureAndUpload();
        }, 3000);

        console.log('Automated capture started - Session:', this.sessionId);
    }

    async captureAndUpload() {
        if (!window.cameraManager || !window.cameraManager.isActive) {
            console.warn('Camera not active, skipping capture');
            return;
        }

        try {
            const frameData = window.cameraManager.captureFrame();
            if (!frameData) {
                console.warn('Failed to capture frame');
                return;
            }

            const timestamp = new Date().toISOString();

            const payload = {
                session_id: this.sessionId,
                timestamp: timestamp,
                frame_data: frameData,
                mode: this.currentMode
            };

            const response = await fetch('/upload_frame', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            const result = await response.json();

            if (result.success) {
                this.frameCounter++;
                console.log(`Frame ${result.frame_number} uploaded successfully`);
            } else {
                console.error('Upload failed:', result.error);
            }
        } catch (error) {
            console.error('Error during capture/upload:', error);
        }
    }

    stopCapture() {
        if (!this.isCapturing) return;

        this.isCapturing = false;

        if (this.captureInterval) {
            clearInterval(this.captureInterval);
            this.captureInterval = null;
        }

        document.getElementById('statusIndicator').textContent = 'Inactive';
        document.getElementById('statusIndicator').className = 'info-value status-inactive';

        const placeholder = document.querySelector('.results-placeholder');
        const emotionResults = document.getElementById('emotionResults');
        const motionResults = document.getElementById('motionResults');

        placeholder.style.display = 'block';
        emotionResults.style.display = 'none';
        motionResults.style.display = 'none';

        document.getElementById('detectedEmotion').textContent = '-';
        document.getElementById('emotionConfidence').textContent = '-';
        document.getElementById('faceCount').textContent = '0';
        document.getElementById('motionStatus').textContent = 'No';
        document.getElementById('motionPercentage').textContent = '0%';
        document.getElementById('motionBar').style.width = '0%';

        console.log('Capture stopped - Total frames:', this.frameCounter);
    }

    setMode(mode) {
        this.currentMode = mode;
        document.getElementById('currentMode').textContent = mode.charAt(0).toUpperCase() + mode.slice(1);

        const placeholder = document.querySelector('.results-placeholder');
        const emotionResults = document.getElementById('emotionResults');
        const motionResults = document.getElementById('motionResults');

        if (mode === 'emotion') {
            placeholder.style.display = 'none';
            emotionResults.style.display = 'flex';
            motionResults.style.display = 'none';
        } else if (mode === 'motion') {
            placeholder.style.display = 'none';
            emotionResults.style.display = 'none';
            motionResults.style.display = 'flex';
        } else {
            placeholder.style.display = 'block';
            emotionResults.style.display = 'none';
            motionResults.style.display = 'none';
        }

        console.log('Detection mode changed to:', mode);
    }

    updateDetectionResults() {
        if (this.currentMode === 'emotion' && window.emotionDetector) {
            const emotion = window.emotionDetector.lastEmotion || 'Detecting...';
            const confidence = window.emotionDetector.lastConfidence || 0;
            const faceCount = window.emotionDetector.faceCount || 0;

            document.getElementById('detectedEmotion').textContent = emotion;
            document.getElementById('emotionConfidence').textContent = `${confidence}%`;
            document.getElementById('faceCount').textContent = faceCount;
        } else if (this.currentMode === 'motion' && window.motionDetector) {
            const motionPercentage = window.motionDetector.lastMotionPercentage || 0;
            const isMotionDetected = motionPercentage >= 5 ? 'Yes' : 'No';

            document.getElementById('motionStatus').textContent = isMotionDetected;
            document.getElementById('motionPercentage').textContent = `${motionPercentage.toFixed(1)}%`;
            document.getElementById('motionBar').style.width = `${motionPercentage}%`;
        }
    }
}

window.captureManager = new CaptureManager();

document.addEventListener('DOMContentLoaded', () => {
    const initCameraBtn = document.getElementById('initCameraBtn');
    const stopCameraBtn = document.getElementById('stopCameraBtn');
    const emotionBtn = document.getElementById('emotionBtn');
    const motionBtn = document.getElementById('motionBtn');
    const statusOverlay = document.getElementById('statusOverlay');

    initCameraBtn.addEventListener('click', async () => {
        const success = await window.cameraManager.initialize();

        if (success) {
            statusOverlay.classList.add('hidden');
            initCameraBtn.style.display = 'none';
            stopCameraBtn.style.display = 'block';
            emotionBtn.disabled = false;
            motionBtn.disabled = false;

            window.captureManager.startCapture();

            console.log('Camera initialized and capture started');
        }
    });

    stopCameraBtn.addEventListener('click', () => {
        window.cameraManager.stop();
        window.captureManager.stopCapture();

        statusOverlay.classList.remove('hidden');
        initCameraBtn.style.display = 'block';
        stopCameraBtn.style.display = 'none';
        emotionBtn.disabled = true;
        motionBtn.disabled = true;

        if (emotionBtn.classList.contains('active')) {
            emotionBtn.classList.remove('active');
            window.emotionDetector.disable();
        }

        if (motionBtn.classList.contains('active')) {
            motionBtn.classList.remove('active');
            window.motionDetector.disable();
        }

        document.getElementById('sessionId').textContent = 'Not Started';
        document.getElementById('currentMode').textContent = 'None';

        console.log('Camera stopped');
    });

    emotionBtn.addEventListener('click', () => {
        if (emotionBtn.classList.contains('active')) {
            emotionBtn.classList.remove('active');
            window.emotionDetector.disable();
            window.captureManager.setMode('none');
        } else {
            emotionBtn.classList.add('active');
            motionBtn.classList.remove('active');
            window.emotionDetector.enable();
            window.motionDetector.disable();
            window.captureManager.setMode('emotion');
        }
    });

    motionBtn.addEventListener('click', () => {
        if (motionBtn.classList.contains('active')) {
            motionBtn.classList.remove('active');
            window.motionDetector.disable();
            window.captureManager.setMode('none');
        } else {
            motionBtn.classList.add('active');
            emotionBtn.classList.remove('active');
            window.motionDetector.enable();
            window.emotionDetector.disable();
            window.captureManager.setMode('motion');
        }
    });
});
