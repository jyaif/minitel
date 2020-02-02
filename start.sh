stty -F /dev/ttyUSB0 4800 istrip cs7 parenb -parodd brkint ignpar icrnl ixon ixany opost onlcr cread hupcl isig icanon echo echoe echok
echo "it works!" >  /dev/ttyUSB0
echo "FNCT+T  A"
echo "FNCT+T  E"
echo "FNCT+P  4"
