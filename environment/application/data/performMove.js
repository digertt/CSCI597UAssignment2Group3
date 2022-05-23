// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
const AWS = require("aws-sdk");
const documentClient = new AWS.DynamoDB.DocumentClient();

const performMove = async ({ gameId, user, board, coords }) => {
    if (coords > 9 || coords < 1) {
    throw new Error('Cannot set heap value below 0')
  }
  coords = coords - 1
  updatemark = 'X'
  if ('user1 = :user')
    updatemark = 'X'
  else
    updatemark = 'O'
  const params = {
    TableName: 'turn-based-game',
    Key: { 
      gameId: gameId
    },
    UpdateExpression: `SET lastMoveBy = :user, ${board[coords]} = :updatemark`,
    ConditionExpression: `(user1 = :user OR user2 = :user) AND lastMoveBy <> :user AND ${board[coords]} == ' '`,
    ExpressionAttributeValues: {
      ':user': user,
      ':coords': coords
    },
    ReturnValues: 'ALL_NEW'
  };
  try {
    const resp = await documentClient.update(params).promise();
    return resp.Attributes;
  } catch (error) {
    console.log("Error updating item: ", error.message);
    throw new Error('Could not perform move')
  }
};

module.exports = performMove
