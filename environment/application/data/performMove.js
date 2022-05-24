// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
const AWS = require("aws-sdk");
const documentClient = new AWS.DynamoDB.DocumentClient();

const performMove = async ({ gameId, user, coords }) => {
    if (coords > 9 || coords < 1) {
    throw new Error('Cannot set heap value below 0')
  }
  coords = coords - 1
  updatemark = 'X'
  try {
    // pull out the userID of user1, who will play X's
    const resp = await documentClient.get({TableName: 'turn-based-game-a2', Key: {gameId: gameId}}).promise();
    console.log(resp);
    user1 = resp.Item.user1;
    user2email = resp.Item.user2;
    if(user2email.includes('@') && user != user1) {
      // this is the first time user2 is going, update their username to be their actual username.
      await documentClient.update({TableName: 'turn-based-game-a2', Key: {gameId: gameId}, UpdateExpression: `SET user2 = :user`, ExpressionAttributeValues: {':user': user}}).promise();
    }
  } catch (error) {
    console.log("Error looking up game: ", error.message);
    throw new Error('Could not perform move')
  }
  if (user1 == user) {
    updatemark = 'X'
  } else {
    updatemark = 'O'
  }
  const params = {
    TableName: 'turn-based-game-a2',
    Key: { 
      gameId: gameId
    },
    UpdateExpression: `SET lastMoveBy = :user, board[${coords}] = :updatemark`,
    ConditionExpression: `(user1 = :user OR user2 = :user) AND lastMoveBy <> :user AND begins_with(board[${coords}], :space)`,
    ExpressionAttributeValues: {
      ':user': user,
      ':updatemark': updatemark,
      ':space': " ",
    },
    ReturnValues: 'ALL_NEW'
  };
  try {
    console.log(user);
    const resp = await documentClient.update(params).promise();
    return resp.Attributes;
  } catch (error) {
    console.log("Error updating item: ", error.message);
    throw new Error('Could not perform move')
  }
};

module.exports = performMove
