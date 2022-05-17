// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
const AWS = require("aws-sdk");
const ses = new AWS.SES();

const sendMessage = async ({ email, message, subject }) => {
  const params = {
    Destination: {
      ToAddresses: [
        email
      ]
    },
    Message: {
      Body: {
        Text: {
          Data: message
        }
      },
      Subject: {
        Data: subject
      }
    },
    Source: 'notify@thebesttictactoe.com',
  }

  return ses.sendEmail(params).promise();
};

module.exports = sendMessage;
