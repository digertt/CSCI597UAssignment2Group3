// Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

const sendMessage = require('./sendMessage')

const handlePostMoveNotification = async ({ game, mover, opponent }) => {
  // Handle when game is finished
  if ((game.board[0] === game.board[1] && game.board[1] === game.board[2] && game.board[2] !== ' ')
      || (game.board[3] === game.board[4] && game.board[4] === game.board[5] && game.board[5] !== ' ')
      || (game.board[6] === game.board[7] && game.board[7] === game.board[8] && game.board[8] !== ' ')
      || (game.board[0] === game.board[3] && game.board[3] === game.board[6] && game.board[6] !== ' ')
      || (game.board[1] === game.board[4] && game.board[4] === game.board[7] && game.board[7] !== ' ')
      || (game.board[2] === game.board[5] && game.board[5] === game.board[8] && game.board[8] !== ' ')
      || (game.board[0] === game.board[4] && game.board[4] === game.board[8] && game.board[8] !== ' ')
      || (game.board[2] === game.board[4] && game.board[4] === game.board[6] && game.board[6] !== ' ')) {
    const winnerMessage = `You beat ${opponent.username} in a game of tic tac toe!`
    const winnerSubject = `You won!`
    const loserMessage = `Ahh, you lost to ${mover.username} in tic tac toe.`
    const loserSubject = `You lost!`
    await Promise.all([
      sendMessage({ email: mover.email, message: winnerMessage, subject: winnerSubject }),
      sendMessage({ email: opponent.email, message: loserMessage, subject: loserSubject })
    ])
  } else {
    const message = `${mover.username} has moved. It's your turn next in Game ID ${game.gameId}!`
    await sendMessage({ email: opponent.email, message, subject: `It's your turn` })
  }
};

module.exports = handlePostMoveNotification;
