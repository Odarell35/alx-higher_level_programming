var apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

// Use jQuery's AJAX function to make the GET request
$.ajax({
  url: apiUrl,
  method: 'GET',
  success: function(data) {
	// Extract the character name from the API response
	var characterName = data.name;

	// Display the character name in the #character div
	$('#character').text(characterName);
  },
  error: function() {
	// Handle errors if the request fails
	$('#character').text('Error fetching character name');
  }
});