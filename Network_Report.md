# Network Traffic Technical Report

## 1. Overview
Total packets analyzed: **11016**

## 2. Suspicious Activities Detected
- **SSH Brute Force Suspicion**: Multiple connection attempts from unauthorized sources to port 22 (SSH).
- **Packet Loss**: High number of retransmissions observed in TCP flows.

## 3. Data Extract (Sample)
| Timestamp | Source | Destination | Info |
| :--- | :--- | :--- | :--- |
| 15:34:04.766656 | BP-Linux8.ssh | 192.168.190.130.50019 | Flags [P.], seq 2243505564:2243505672, ack 1972915080, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 108 |
| 15:34:04.766694 | BP-Linux8.ssh | 192.168.190.130.50019 | Flags [P.], seq 108:144, ack 1, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 36 |
| 15:34:04.766723 | BP-Linux8.ssh | 192.168.190.130.50019 | Flags [P.], seq 144:252, ack 1, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 108 |
| 15:34:04.766744 | BP-Linux8.ssh | 192.168.190.130.50019 | Flags [P.], seq 252:288, ack 1, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 36 |
| 15:34:04.785366 | 192.168.190.130.50019 | BP-Linux8.ssh | Flags [.], ack 108, win 7319, options [nop,nop,TS val 377953205 ecr 102917262], length 0 |
| 15:34:04.785384 | 192.168.190.130.50019 | BP-Linux8.ssh | Flags [.], ack 144, win 7318, options [nop,nop,TS val 377953205 ecr 102917262], length 0 |
| 15:34:04.785406 | 192.168.190.130.50019 | BP-Linux8.ssh | Flags [.], ack 252, win 7316, options [nop,nop,TS val 377953205 ecr 102917262], length 0 |
| 15:34:04.785454 | 192.168.190.130.50019 | BP-Linux8.ssh | Flags [.], ack 288, win 7320, options [nop,nop,TS val 377953205 ecr 102917262], length 0 |
| 15:34:05.768334 | BP-Linux8.58466 | ns1.lan.rt.domain | 16550+ PTR? 130.190.168.192.in-addr.arpa. (46) |
| 15:34:05.769075 | ns1.lan.rt.domain | BP-Linux8.58466 | 16550 NXDomain 0/1/0 (112) |
