<div id="time"></div>

<script>
    function updateTime() {
        var currentTime = new Date();
        var hours = currentTime.getHours();
        var minutes = currentTime.getMinutes();
        var seconds = currentTime.getSeconds();

        // Добавляем ведущий 0, если число меньше 10
        minutes = (minutes < 10 ? "0" : "") + minutes;
        seconds = (seconds < 10 ? "0" : "") + seconds;

        var timeString = hours + ":" + minutes + ":" + seconds;
        document.getElementById("time").innerHTML = timeString;
    }

    updateTime();
    setInterval(updateTime, 1000); // Обновляем время каждую секунду
</script>