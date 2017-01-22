document.addEventListener("DOMContentLoaded", function (event) {
    var g = new JustGage({
        id: "gauge",
        value: 67,
        min: 0,
        max: 100,
        title: "Visitors"
    });
    var gg1 = new JustGage({
        id: "gg1",
        formatNumber: true,
        counter: true
    });

    document.getElementById('gg1_refresh').addEventListener('click', function () {
        gg1.refresh(getRandomInt(0, 300));
        return false;
    });

    var gg2 = new JustGage({
        id: "gg2",
        formatNumber: true,
        counter: true
    });

    document.getElementById('gg2_refresh').addEventListener('click', function () {
        gg2.refresh(getRandomInt(0, 250));
        return false;
    });
    var gg3 = new JustGage({
        id: "gg3",
        formatNumber: true,
        counter: true
    });

    document.getElementById('gg3_refresh').addEventListener('click', function () {
        gg3.refresh(getRandomInt(0, 1300));
        return false;
    });
});