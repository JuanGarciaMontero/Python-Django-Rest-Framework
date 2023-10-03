window.onload = function () {
    myVar = setInterval(myTimer, 1000);
        myVar2 = setInterval(myDate, 1000);
        function myTimer() {
            const d = new Date();
            document.getElementById("demo").innerHTML = d.toLocaleTimeString();
        }
        function myDate() {
            const d = new Date();
            document.getElementById("demo2").innerHTML = d.toLocaleDateString();
        }
}
