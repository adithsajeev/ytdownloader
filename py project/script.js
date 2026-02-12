// Game State
const gameState = {
    currentStage: 1,
    answer: 7,
    guesses: 0,
    anniversary: 16,
    duration: "2.9",
    magicWord: "love"
};

// Special Dates Messages
const specialDates = {
    7: "Its your roll number bby",
    16: "Its our anniversary day",
    50: "Half century",
    71: "Its my roll numberrr"
};

// Stage Management
function goToStage(stage) {
    // Hide all stages
    document.querySelectorAll('.stage').forEach(s => {
        s.classList.remove('active');
    });
    
    // Show target stage
    const targetStage = document.getElementById(`stage${stage}`);
    targetStage.classList.add('active');
    
    // Clear inputs
    const inputs = targetStage.querySelectorAll('input');
    inputs.forEach(input => input.value = '');
    
    // Clear feedbacks
    const feedbacks = targetStage.querySelectorAll('.feedback');
    feedbacks.forEach(feedback => {
        feedback.textContent = '';
        feedback.className = 'feedback';
    });
    
    // Focus first input
    if (inputs.length > 0) {
        inputs[0].focus();
    }
    
    gameState.currentStage = stage;
}

// Stage 1: Number Guessing
function submitGuess() {
    const guessInput = document.getElementById('guessInput');
    const feedback = document.getElementById('feedback');
    const guessCount = document.getElementById('guessCount');
    const specialMessage = document.getElementById('specialMessage');
    const guess = guessInput.value.trim();
    
    if (!guess) {
        feedback.textContent = 'Please enter a valid number!';
        feedback.className = 'feedback error';
        return;
    }
    
    if (isNaN(guess)) {
        feedback.textContent = 'Pottathi correct number kodthe 😤';
        feedback.className = 'feedback error';
        guessInput.value = '';
        return;
    }
    
    const guessNum = parseInt(guess);
    gameState.guesses++;
    guessCount.textContent = `Guesses: ${gameState.guesses}`;
    
    // Check for special dates
    specialMessage.textContent = '';
    if (specialDates[guessNum]) {
        specialMessage.textContent = specialDates[guessNum];
        createConfetti();
    }
    
    // Check range
    if (guessNum > 100 || guessNum < 1) {
        feedback.textContent = 'Guess the number in the range (1-100)! 🚫';
        feedback.className = 'feedback error';
        guessInput.value = '';
        return;
    }
    
    // Check answer
    if (guessNum > gameState.answer) {
        feedback.textContent = 'Answer = Too high! Try lower 📉';
        feedback.className = 'feedback error';
    } else if (guessNum < gameState.answer) {
        feedback.textContent = 'Answer = Too low! Try higher 📈';
        feedback.className = 'feedback error';
    } else {
        feedback.textContent = `🎉 Your answer is correct! ${gameState.answer} is the number! 🎉`;
        feedback.className = 'feedback success';
        
        // Celebrate
        createConfetti();
        playSound('success');
        
        // Move to next stage after delay
        setTimeout(() => {
            goToStage(2);
        }, 1500);
    }
    
    guessInput.value = '';
}

// Stage 2: Secret Key
function submitKey() {
    const keyInput = document.getElementById('keyInput');
    const keyFeedback = document.getElementById('keyFeedback');
    const key = keyInput.value.trim();
    
    if (!key) {
        keyFeedback.textContent = 'Please enter a key!';
        keyFeedback.className = 'feedback error';
        return;
    }
    
    if (key === String(gameState.answer)) {
        keyFeedback.textContent = '😘 Ammadi you found it! Arada paranje kunjinu bhudhi illa enn ehh ehh 😘';
        keyFeedback.className = 'feedback success';
        createConfetti();
        playSound('success');
        
        setTimeout(() => {
            goToStage(3);
        }, 1500);
    } else {
        keyFeedback.textContent = 'Pottathi avaleee angott alogich nokkk 🤔';
        keyFeedback.className = 'feedback error';
        keyInput.value = '';
    }
}

// Stage 3: Anniversary Date
function submitDate() {
    const dateInput = document.getElementById('dateInput');
    const dateFeedback = document.getElementById('dateFeedback');
    const date = dateInput.value.trim();
    
    if (!date) {
        dateFeedback.textContent = 'Please enter a date!';
        dateFeedback.className = 'feedback error';
        return;
    }
    
    if (parseInt(date) === gameState.anniversary) {
        dateFeedback.textContent = '✨ ---------THAKKUDUU😚😚😚💕--------- ✨';
        dateFeedback.className = 'feedback success';
        createConfetti();
        playSound('success');
        
        setTimeout(() => {
            goToStage(4);
        }, 1500);
    } else {
        dateFeedback.textContent = 'NO MORE GAMES BYE 😠😡😤';
        dateFeedback.className = 'feedback error';
        dateInput.value = '';
    }
}

// Stage 4: Duration Together
function submitDuration() {
    const durationInput = document.getElementById('durationInput');
    const durationFeedback = document.getElementById('durationFeedback');
    const duration = durationInput.value.trim();
    
    if (!duration) {
        durationFeedback.textContent = 'Please enter the duration!';
        durationFeedback.className = 'feedback error';
        return;
    }
    
    if (duration === gameState.duration) {
        durationFeedback.textContent = '😊 You are my bbyyy Ummmaa 😊';
        durationFeedback.className = 'feedback success';
        createConfetti();
        playSound('success');
        
        setTimeout(() => {
            goToStage(5);
        }, 1500);
    } else {
        durationFeedback.textContent = 'KOLAAAAAMMMMM kolaam poyi kankk koott 😢';
        durationFeedback.className = 'feedback error';
        durationInput.value = '';
    }
}

// Stage 5: Magic Word
function submitWord() {
    const wordInput = document.getElementById('wordInput');
    const wordFeedback = document.getElementById('wordFeedback');
    const word = wordInput.value.trim();
    
    if (!word) {
        wordFeedback.textContent = 'Please enter the word!';
        wordFeedback.className = 'feedback error';
        return;
    }
    
    if (word.toLowerCase() === gameState.magicWord) {
        wordFeedback.textContent = '✨ Its time for the wish! ✨';
        wordFeedback.className = 'feedback success';
        createBigConfetti();
        playSound('success');
        
        setTimeout(() => {
            goToStage(6);
        }, 1500);
    } else {
        wordFeedback.textContent = 'Enter the correct word! 🤔';
        wordFeedback.className = 'feedback error';
        wordInput.value = '';
    }
}

// Confetti Animation
function createConfetti() {
    for (let i = 0; i < 15; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.textContent = ['💖', '💕', '✨', '🎉', '💝'][Math.floor(Math.random() * 5)];
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.top = '-10px';
        confetti.style.fontSize = (Math.random() * 20 + 20) + 'px';
        confetti.style.animationDelay = (Math.random() * 0.5) + 's';
        document.body.appendChild(confetti);
        
        // Remove after animation
        setTimeout(() => confetti.remove(), 3000);
    }
}

function createBigConfetti() {
    for (let i = 0; i < 30; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.textContent = ['💖', '💕', '✨', '🎉', '💝', '🌟', '💐'][Math.floor(Math.random() * 7)];
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.top = '-10px';
        confetti.style.fontSize = (Math.random() * 30 + 25) + 'px';
        confetti.style.animationDelay = (Math.random() * 0.8) + 's';
        document.body.appendChild(confetti);
        
        // Remove after animation
        setTimeout(() => confetti.remove(), 3500);
    }
}

// Sound Effects (Optional)
function playSound(type) {
    // Create a simple beep using Web Audio API
    try {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        if (type === 'success') {
            oscillator.frequency.value = 800;
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
        } else {
            oscillator.frequency.value = 400;
            gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
        }
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.1);
    } catch (e) {
        // Audio not supported, ignore
    }
}

// Keyboard Support
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            const stage = gameState.currentStage;
            if (stage === 1) submitGuess();
            else if (stage === 2) submitKey();
            else if (stage === 3) submitDate();
            else if (stage === 4) submitDuration();
            else if (stage === 5) submitWord();
        }
    });
    
    // Start with stage 1
    goToStage(1);
});
