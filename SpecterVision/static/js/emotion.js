class EmotionDetector {
    constructor() {
        this.model = null;
        this.isEnabled = false;
        this.isLoading = false;
        this.lastEmotion = null;
        this.lastConfidence = 0;
        this.faceCount = 0;
    }

    async loadModel() {
        if (this.model || this.isLoading) return;

        this.isLoading = true;
        console.log('Loading face landmarks detection model...');

        try {
            this.model = await faceLandmarksDetection.createDetector(
                faceLandmarksDetection.SupportedModels.MediaPipeFaceMesh,
                {
                    runtime: 'tfjs',
                    maxFaces: 5,
                    refineLandmarks: false
                }
            );
            console.log('Face landmarks detection model loaded successfully');
        } catch (error) {
            console.error('Failed to load face detection model:', error);
        } finally {
            this.isLoading = false;
        }
    }

    async enable() {
        this.isEnabled = true;
        if (!this.model) {
            await this.loadModel();
        }
        console.log('Emotion detection enabled');
    }

    disable() {
        this.isEnabled = false;
        console.log('Emotion detection disabled');
    }

    analyzeEmotion(keypoints) {
        const leftMouthCorner = keypoints[61];
        const rightMouthCorner = keypoints[291];
        const topLip = keypoints[13];
        const bottomLip = keypoints[14];
        const leftEye = keypoints[33];
        const rightEye = keypoints[263];
        const leftEyebrow = keypoints[70];
        const rightEyebrow = keypoints[300];
        const noseTip = keypoints[1];

        const mouthWidth = Math.sqrt(
            Math.pow(rightMouthCorner[0] - leftMouthCorner[0], 2) +
            Math.pow(rightMouthCorner[1] - leftMouthCorner[1], 2)
        );

        const mouthHeight = Math.abs(topLip[1] - bottomLip[1]);
        const mouthAspectRatio = mouthHeight / mouthWidth;

        const mouthCenterY = (leftMouthCorner[1] + rightMouthCorner[1]) / 2;
        const mouthBaseline = bottomLip[1];
        const mouthCurvature = mouthBaseline - mouthCenterY;

        const eyeDistance = Math.sqrt(
            Math.pow(rightEye[0] - leftEye[0], 2) +
            Math.pow(rightEye[1] - leftEye[1], 2)
        );

        const leftEyebrowHeight = leftEyebrow[1] - leftEye[1];
        const rightEyebrowHeight = rightEyebrow[1] - rightEye[1];
        const avgEyebrowHeight = (leftEyebrowHeight + rightEyebrowHeight) / 2;

        const normalizedEyebrowHeight = avgEyebrowHeight / eyeDistance;

        let emotion = 'Neutral';
        let confidence = 0;

        if (mouthCurvature < -2 && mouthAspectRatio > 0.15) {
            emotion = 'Happy';
            confidence = Math.min(95, 60 + Math.abs(mouthCurvature) * 5);
        }
        else if (mouthAspectRatio > 0.35 && normalizedEyebrowHeight < -0.08) {
            emotion = 'Surprised';
            confidence = Math.min(95, 65 + mouthAspectRatio * 80);
        }
        else if (normalizedEyebrowHeight < -0.12 && mouthAspectRatio < 0.15) {
            emotion = 'Angry';
            confidence = Math.min(92, 60 + Math.abs(normalizedEyebrowHeight) * 200);
        }
        else if (mouthCurvature > 1.5 && normalizedEyebrowHeight < -0.05) {
            emotion = 'Sad';
            confidence = Math.min(88, 55 + mouthCurvature * 10);
        }
        else if (mouthAspectRatio > 0.25 && normalizedEyebrowHeight < -0.06) {
            emotion = 'Fearful';
            confidence = Math.min(85, 55 + mouthAspectRatio * 60);
        }
        else if (mouthCurvature > 0 && mouthAspectRatio < 0.12) {
            emotion = 'Disgusted';
            confidence = Math.min(80, 50 + mouthCurvature * 8);
        }
        else {
            emotion = 'Neutral';
            confidence = 75;
        }

        return { emotion, confidence: Math.round(confidence) };
    }

    detect(canvas, ctx) {
        if (!this.isEnabled || !this.model) return;

        this.model.estimateFaces(canvas, {
            flipHorizontal: false
        }).then(faces => {
            this.faceCount = faces.length;

            if (faces.length > 0) {
                faces.forEach(face => {
                    const box = face.box;
                    const keypoints = face.keypoints;

                    ctx.strokeStyle = '#00ff00';
                    ctx.lineWidth = 3;
                    ctx.strokeRect(box.xMin, box.yMin, box.width, box.height);

                    const { emotion, confidence } = this.analyzeEmotion(keypoints);

                    this.lastEmotion = emotion;
                    this.lastConfidence = confidence;

                    const labelText = `${emotion} (${confidence}%)`;
                    ctx.font = 'bold 18px Arial';
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                    const textMetrics = ctx.measureText(labelText);
                    const textWidth = textMetrics.width;
                    const textHeight = 24;
                    const padding = 8;

                    ctx.fillRect(
                        box.xMin - 2,
                        box.yMin - textHeight - padding - 5,
                        textWidth + padding * 2,
                        textHeight + padding
                    );

                    ctx.fillStyle = '#ffffff';
                    ctx.fillText(labelText, box.xMin + padding - 2, box.yMin - 10);
                });
            } else {
                this.lastEmotion = null;
                this.lastConfidence = 0;
            }
        }).catch(error => {
            console.error('Emotion detection error:', error);
        });
    }
}

window.emotionDetector = new EmotionDetector();
