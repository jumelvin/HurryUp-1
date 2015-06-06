var input = document.getElementById('searchTextField');

autocomplete = new google.maps.places.Autocomplete(input, { types:
                                                           ['geocode'] } );

google.maps.event.addListener(autocomplete, 'place_changed', function(){
    var place = autocomplete.getPlace();

});