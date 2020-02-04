function getSearchValue(){
    search_city = document.getElementById('search').value;
    window.location.href = "/buy/" + "?city="+search_city;
}

window.onload = function(){
        var url_str = (window.location.href);
        var url = new URL(url_str);
        var textCity = document.getElementById("city");
        if (textCity != null) {
            var searchCity = url.searchParams.get("city");
            document.getElementById("city").value = searchCity;
        }
}

$(document).ready(function(){
    $("#search_prop").click(function(){
        var city = $("#city").val();
        var prop_type = $("#proptype option:selected:enabled").text();
        var beds = $("#beds option:selected:enabled").text();
        $.ajax({
            'method': 'GET',
            'url': '.',  // submit to the same url
            'data': {city: city, ptype: prop_type, beds: beds},  // pass here any data to the server.
            success: function(data) {
                // This function will run when server returns data
                var props = $(data).find('#properties').html();
                $('#properties').html(props);
            }
    });
     });
});

$(document).ready(function(){
    $("#search_agent").click(function(){
        var city = $("#agent_city").val();
        var name = $("#agent_name").val();
        $.ajax({
            'method': 'GET',
            'url': '.',  // submit to the same url
            'data': {city: city, name: name},  // pass here any data to the server.
            success: function(data) {
                // This function will run when server returns data
                var agents = $(data).find('#agents').html();
                $('#agents').html(agents);
            }
    });
     });
});