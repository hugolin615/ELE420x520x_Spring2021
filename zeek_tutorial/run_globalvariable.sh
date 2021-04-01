sudo rm *.log

zeek -Cr data_aggregator.pcap ./dnp3m_analyzer/dnp3m.hlto ./global_variable.zeek
