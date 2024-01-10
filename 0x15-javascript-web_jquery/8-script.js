var apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Use jQuery's AJAX function to make the GET request
    $.ajax({
      url: apiUrl,
      method: 'GET',
      success: function(data) {
        // Iterate through each movie and append its title to the #list_movies ul
        $.each(data.results, function(index, movie) {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      },
      error: function() {
        // Handle errors if the request fails
        $('#list_movies').append('<li>Error fetching movie titles</li>');
      }
    });