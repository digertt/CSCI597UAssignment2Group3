// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
const AWS = require('aws-sdk')
const documentClient = new AWS.DynamoDB.DocumentClient()

const performMove = async ({ gameId, user, changedHeap, changedHeapValue }) => {
  if (changedHeapValue > 9 || changedHeapValue < 1) {
    throw new Error('Cannot set heap value below 0')
  }
  changedHeapValue = changedHeapValue - 1
  if ('user1 = :user')
    updatemark = 'X'
  else
    updatemark = 'O'
  const params = {
    TableName: 'turn-based-game',
    Key: { 
      gameId: gameId
    },
    UpdateExpression: `SET lastMoveBy = :user, ${changedHeap[changedHeapValue]} = :updatemark`,
    ConditionExpression: `(user1 = :user OR user2 = :user) AND lastMoveBy <> :user AND ${changedHeap[changedHeapValue]} == ' '`,
    ExpressionAttributeValues: {
      ':user': user,
      ':changedHeapValue': changedHeapValue,
    },
    ReturnValues: 'ALL_NEW'
  }
  try {
    const resp = await documentClient.update(params).promise()
    console.log('Updated game: ', resp.Attributes)
  } catch (error) {
    console.log('Error updating item: ', error.message)
  }
}

performMove({ gameId: '5b5ee7d8', user: 'theseconduser', changedHeap: 'board', changedHeapValue: 3 })
