class MotionDetector {
    constructor() {
        this.isEnabled = false;
        this.previousFrame = null;
        this.motionThreshold = 5;
        this.pixelDiffThreshold = 30;
        this.lastMotionPercentage = 0;
    }

    enable() {
        this.isEnabled = true;
        this.previousFrame = null;
        console.log('Motion detection enabled');
    }

    disable() {
        this.isEnabled = false;
        this.previousFrame = null;
        console.log('Motion detection disabled');
    }

    detect(canvas, ctx) {
        if (!this.isEnabled) return;

        const currentFrame = ctx.getImageData(0, 0, canvas.width, canvas.height);

        if (this.previousFrame) {
            const diff = this.calculateDifference(
                this.previousFrame.data,
                currentFrame.data,
                canvas.width,
                canvas.height
            );

            this.lastMotionPercentage = diff.motionPercentage;

            if (diff.motionPercentage >= this.motionThreshold) {
                this.highlightMotion(ctx, diff.motionMap, canvas.width, canvas.height, diff.motionPercentage);
            }
        } else {
            this.lastMotionPercentage = 0;
        }

        this.previousFrame = currentFrame;
    }

    calculateDifference(prevData, currData, width, height) {
        const motionMap = [];
        let motionPixels = 0;
        const totalPixels = width * height;

        for (let i = 0; i < prevData.length; i += 4) {
            const diff = Math.abs(prevData[i] - currData[i]) +
                         Math.abs(prevData[i + 1] - currData[i + 1]) +
                         Math.abs(prevData[i + 2] - currData[i + 2]);

            if (diff > this.pixelDiffThreshold) {
                motionMap.push(i / 4);
                motionPixels++;
            }
        }

        const motionPercentage = (motionPixels / totalPixels) * 100;

        return { motionMap, motionPixels, motionPercentage };
    }

    highlightMotion(ctx, motionMap, width, height, motionPercentage) {
        ctx.fillStyle = 'rgba(255, 0, 0, 0.4)';

        motionMap.forEach(pixelIndex => {
            const x = pixelIndex % width;
            const y = Math.floor(pixelIndex / width);
            ctx.fillRect(x, y, 1, 1);
        });

        const bannerText = `MOTION DETECTED - ${motionPercentage.toFixed(1)}%`;
        ctx.font = 'bold 20px Arial';

        const textMetrics = ctx.measureText(bannerText);
        const textWidth = textMetrics.width;
        const bannerHeight = 40;
        const bannerY = 50;

        ctx.fillStyle = 'rgba(255, 193, 7, 0.9)';
        ctx.fillRect(10, bannerY, textWidth + 30, bannerHeight);

        ctx.strokeStyle = '#ff0000';
        ctx.lineWidth = 3;
        ctx.strokeRect(10, bannerY, textWidth + 30, bannerHeight);

        ctx.fillStyle = '#000000';
        ctx.fillText(bannerText, 25, bannerY + 27);

        const barWidth = width - 40;
        const barHeight = 15;
        const barX = 20;
        const barY = height - 40;

        ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
        ctx.fillRect(barX, barY, barWidth, barHeight);

        ctx.fillStyle = '#ff0000';
        const fillWidth = (motionPercentage / 100) * barWidth;
        ctx.fillRect(barX, barY, fillWidth, barHeight);

        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.strokeRect(barX, barY, barWidth, barHeight);
    }
}

window.motionDetector = new MotionDetector();
