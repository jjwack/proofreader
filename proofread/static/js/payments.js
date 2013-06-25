$('.pay-stripe').click(function(){
  var token = function(res){
    var $input = $('<input type=hidden name=stripeToken />').val(res.id);
    $('form').append($input).submit();
  };

  console.log(this.value);

  StripeCheckout.open({
    key:         'pk_test_czwzkTp2tactuLOEOqbMTRzG',
    // address:     true,
    amount:      5000,
    currency:    'usd',
    name:        'Joes Pistachios',
    description: 'A bag of Pistachios',
    panelLabel:  'Checkout',
    token:       token
  });

  return false;
});


$("#custom-amt").keyup(function() {
    if ($.isNumeric(this.value)) {
        var rounded = Number(this.value).toFixed(2);
        $("#custom-btn").attr("value", rounded*100);
        $("#custom-btn").text("Add $"+rounded);
    }
    else if (this.value) {
        $("#custom-alert").removeClass("hidden");
    }
});

$("#custom-alert").click(function() {
    $("#custom-alert").addClass("hidden");
});