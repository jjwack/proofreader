$('.pay-stripe').click(function(){

  var amt = this.value;
  var str_amt = Number(this.value/100).toFixed(2);

  var $input = $('<input type=hidden name=amount />').val(amt);
  $('form').append($input);


  var token = function(res){
    var $input = $('<input type=hidden name=stripeToken />').val(res.id);
    $('form').append($input).submit();
  };

  StripeCheckout.open({
    key:         'pk_test_kjnZxihVhQmCxF40zx3La3bC',
    // address:     true,
    amount:      amt,
    currency:    'usd',
    name:        'Proofread Me',
    description: 'Add $'+str_amt+' to your account.',
    panelLabel:  'Add',
    token:       token
  });

  return false;
});

$("#request-amt").text(function(){
    var rounded = Number(this.value).toFixed(2);
    $(this).text("Add $"+rounded/100);
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