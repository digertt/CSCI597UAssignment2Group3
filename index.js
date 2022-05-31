const AWS = require('aws-sdk');
const DDB = new AWS.DynamoDB.DocumentClient({
    version: '2012-08-10',
    region: 'us-west-1'
});

exports.handler = async (event) => {
    try{
        const {message} = event;
        const curBody = JSON.parse(message.body); //we may need to get multiple items
        
        const curPost = {
            TableName: 'our-table-name',
            Item:{
                username: curBody.username,
                title: curBody.title,
                content: curBody.content
            }
        };
        await DDB.put(curPost).promise();
    }
    
    catch(error){
        console.log(error);
        return;
    }
    
};
