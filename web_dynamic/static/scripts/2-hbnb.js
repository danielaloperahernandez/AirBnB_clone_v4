$('document').ready(() => {
  $.get('http://0.0.0.0:5001/api/v1/status/', (data, status) => {
    if (status === 'success') {
      $('DIV#api_status').addClass('available');
    } else {
      $('DIV#api_status').removeClass('avaliable');
    }
  });

  const amenities = {};

  $('div.amenities li input').change(function () {
    if ($(this).is(':checked')) {
      amenities[($(this).attr('data-id'))] = $(this).attr('data-name');
    } else {
      delete amenities[($(this).attr('data-id'))];
    }
    $('div.amenities h4').text(Object.values(amenities).join(', '));
  });
});
