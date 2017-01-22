document.addEventListener("DOMContentLoaded", function (event) {

  $( function() {
    var d = new Date();
    var h = ('0' + d.getHours()).slice(-2);
    var m = d.getMinutes();
    function formatAMPM(date) {
  var hours = ('0' + d.getHours()).slice(-2);
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}
    $( "#slider-range-min" ).slider({
      range: "min",
      value: 7,
      min: 1,
      max: 22,
      step: 1,
      slide: function( event, ui ) {
        $( "#amount" ).val( Times[ui.value] );
        gg1.refresh(getRandomInt(0, 300));
        gg2.refresh(getRandomInt(0, 250));
        gg3.refresh(getRandomInt(0, 1300));
      }
      
    });
    $( "#amount" ).val( formatAMPM(d) );
  } );

Times = ['07:00 AM','07:30 AM','08:00 AM','08:30 AM','09:00 AM',
         '09:30 AM','10:00 AM','10:30 AM','11:00 AM','11:30 AM',
         '12:00 PM','12:30 PM','01:00 PM','01:30 PM','02:00 PM',
         '02:30 PM','03:00 PM','03:30 PM','04:00 PM','04:30 PM',
         '05:00 PM','05:30 PM','06:00 PM','06:30 PM','07:00 PM',
         '07:30 PM','8:00 PM']

West  = [02, 23, 63, 23, 55, 53, 21, 16, 50, 22, 60, 70, 60, 43, 
         43, 11, 25, 40, 45, 60, 80, 30, 30, 20, 10, 10, 02];
North = [13, 22, 84, 16, 71, 02, 86, 67, 55, 91, 31, 94, 47, 96, 
         39, 68, 19, 74, 65, 43, 33, 90, 70, 50, 50, 30, 03];
East  = [02, 29, 05, 05, 02, 03, 10, 09, 03, 20, 07, 70, 23, 46, 
         75, 41, 23, 54, 41, 11, 40, 50, 40, 60, 40, 30, 20];

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Times,
    datasets: [{
      label: 'West Lot',
      data: West,
      backgroundColor: "rgba(255, 0, 0, 0.4)"
    }, {
      label: 'North Lot',
      data: North,
      backgroundColor: "rgba(0, 255, 0, 0.2)"
    }, {
      label: 'East Lot',
      data: East,
      backgroundColor: "rgba(0, 0, 255, 0.3)"
    }]
  }
});


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