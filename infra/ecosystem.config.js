const { execSync } = require('child_process');
module.exports = {
    apps : [{
        name: 'API',
        script: 'npm',
        args: 'run envstart',
        
        // Options reference: https://pm2.io/doc/en/runtime/reference/ecosystem-file/
        instances: 1,
        autorestart: true,
        watch: false,
        max_memory_restart: '1G',
        env_production: {
            NODE_ENV: 'production'
        }
    }],
    
    deploy : {
        production : {
            user: 'ec2-user',
            key: '~/.ssh/BGCDev.pem',
            host : 'noplp.boardgamecomponion.com',
            ref  : 'master',
            repo : 'https://github.com/FServais/noplp.git',
            path : '/home/ec2-user/noplp',
            'post-deploy' : '\
            export CERTDOMAIN=noplp.boardgamecomponion.com && \
                npm install && \
                pm2 start npm -- run envstart && \
                sudo nginx -s reload'
        }
    }
};