// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

const sendMessage = require('./sendMessage')

const handlePostMoveNotification = async ({ game, mover, opponent }) => {
  // Handle when game is finished
  if (game.heap1 == 0 && game.heap2 == 0 && game.heap3 == 0) {
    const winnerMessage = `You beat ${mover.username} in a game of Nim!`
    const winnerSubject = `You won!`
    const loserMessage = `Ahh, you lost to ${opponent.username} in Nim.`
    const loserSubject = `You lost!`
    await Promise.all([
      sendMessage({ email: opponent.email, message: winnerMessage, subject: winnerSubject }),
      sendMessage({ email: mover.email, message: loserMessage, subject: loserSubject })
    ])

    return
  }

  const message = `${mover.username} has moved. It's your turn next in Game ID ${game.gameId}!`
  await sendMessage({ email: opponent.email, message, subject: `It's your turn` })
};

module.exports = handlePostMoveNotification;