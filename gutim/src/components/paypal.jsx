import React, { useEffect } from 'react';

export default function Paypal(props) {
  useEffect(() => {
    window.paypal
      .Buttons({
        createOrder: function (data, actions) {
          // This function sets up the details of the transaction, including the amount and line item details.
          return actions.order.create({
            purchase_units: [
              {
                amount: {
                  value: props.price,
                },
              },
            ],
          });
        },
        onApprove: function (data, actions) {
          // This function captures the funds from the transaction.
          return actions.order.capture().then(function (details) {
            // This function shows a transaction success message to your buyer.
            alert('Transaction completed by ' + details.payer.name.given_name);
          });
        },
        onCancel: function (data) {
          // Show a cancel page, or return to cart
          alert('You Cancled The Payment');
        },
        onError: function (err) {
          // For example, redirect to a specific error page
          console.log(err);
        },
      })
      .render(`#${props.name}`);
  }, []);
  return (
    <React.Fragment>
      <div id={props.name}>Paypal</div>
    </React.Fragment>
  );
}
/**
 * sb-viwrl20314967@personal.example.com
 * Ob4q#Q>h
 */
