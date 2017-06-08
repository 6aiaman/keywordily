$(document).ready(function() {

  // DATATABLE
    // var mydata;

    var table = $('#data_kw').DataTable( {
        scrollY:'75vh',
        searching: false,
        scrollCollapse: true,
        paging: false,
        columnDefs: [
            {
                "targets": [ 0 ],
                "visible": false
            }
        ],
        dom: '<"top">rt<"bottom"B><"clear">',
        buttons: ['copy', 'csv'], // Download the table

        createdRow: function( row, data, index ) { // PPC Color Scale
		 //    var PPC_value = Number(data[5])
		 //    if ( PPC_value < 0.2 ) {
		 //    	$('td', row).eq(4).addClass('excellent');
			// } else if (PPC_value < 0.4) {
			//     $('td', row).eq(4).addClass('good');
			// } else if (PPC_value < 0.6) {
			//     $('td', row).eq(4).addClass('normal');
			// } else if (PPC_value < 0.8) {
			//     $('td', row).eq(4).addClass('bad');
			// } else {
			//     $('td', row).eq(4).addClass('terrible');
			// } 
		  }
    });


    // $('#data_kw tbody').on('click', 'tr', function () {
    //     var data = table.row(this).data();
    //     $('p#keyword_overview').text(data[1]);
    //     $('p#intent_overview').text(data[2]);
    //     $('p#volume_overview').text(data[3]);
    //     $('p#cpc_overview').text(data[4]);
    //     $('p#ppc_overview').text(data[5]);
    //     $('p#trend_overview').text(data[6]);
      

    //   // TREND CHART
    //     var trendchart = document.getElementById("TrendChart");
    //     var trenddata = [8119915, 7410855, 3743361, 7248228, 5383867, 2727040, 1171094, 4616212, 6685099, 1961761, 1101025, 2774209];
    //     var trendlabels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    //     var TrendChart = new Chart(trendchart, {
    //         type: 'line',
    //         data: {
    //             labels: trendlabels,
    //             datasets: [{
    //                 label: 'Search Trend',    
    //                 data: trenddata,
    //                 backgroundColor: [
    //                     'rgba(255, 99, 132, 0.2)'
    //                 ],
    //                 borderColor: [
    //                     'rgba(255,99,132,1)'
    //                 ],
    //                 borderWidth: 0
    //             }]
    //         }
    //     });
    // });
});

