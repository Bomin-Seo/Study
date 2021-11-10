const finals = '18 june 2021';

function formatTime(time){
    return time < 10 ? '0' + time : time;
}

function countdown() {
    const finalsDate = new Date(finals);
    const currentDate = new Date();

    const totalSeconds = (finalsDate - currentDate) / 1000;
    const days = Math.floor(totalSeconds / 3600 / 24);
    const hours = Math.floor(totalSeconds / 3600) % 24;
    const minutes = Math.floor(totalSeconds / 60) % 60;
    const seconds = Math.floor(totalSeconds) % 60;

    document.getElementById('days').innerText = formatTime(days);
    document.getElementById('hours').innerText = formatTime(hours);
    document.getElementById('minutes').innerText = formatTime(minutes);
    document.getElementById('seconds').innerText = formatTime(seconds);
}

setInterval(countdown, 1000);

