
ipAddress = '169.254.100.57';  
port = 5050;  

tcpipClient = tcpip(ipAddress, port);

while true  
    fopen(tcpipClient);
    if strcmp(tcpipClient.Status, 'open')
        pause(1);
        % Receive 
        if tcpipClient.BytesAvailable >0
            data = fread(tcpipClient, tcpipClient.BytesAvailable, 'char');
            receivedData = char(data');
            disp(receivedData);
        else
            pause(2)
        end
    else
        pause(2);
    end
    fclose(tcpipClient);
    pause(0.1);
end
% Close connection
%fclose(tcpipClient);
%delete(tcpipClient);