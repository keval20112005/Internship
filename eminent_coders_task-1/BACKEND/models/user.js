const mongoose = require('mongoose');

const userschema = new mongoose.Schema({
    username:
    {
        type: String,
        required: true,
        unique: true
    },
    password:
    {
        type: String,
        required: true,
    },
    role:
    {
        type: String,
        enum: ['user', 'admin'],
        default: 'user' 
    }
});

module.exports = mongoose.model('User', userschema);