#!/usr/bin/node
function myfunction()
{
    const args=process.argv.length;
    if (args != 0)
        console.log('Arguments found');
    else if (args==1)
        console.log('No argument');
    else
        console.log('Arguments found');
}
myfunction();
