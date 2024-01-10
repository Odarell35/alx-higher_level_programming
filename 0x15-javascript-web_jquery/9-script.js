var apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Use jQuery's AJAX function to make the GET request
$.ajax({
  url: apiUrl,
  method: 'GET',
  success: function(data) {
	// Display the translation of "hello" in the #hello div
	$('#hello').text(data.hello);
  },
  error: function() {
	// Handle errors if the request fails
	$('#hello').text('Error fetching translation');
  }
});