# passgen

Generate random passwords that meet basic complexity requirements: at least one lowercase, one uppercase and one number. Optionally special characters can be included too.

## Usage

    from passgen import passgen
	pw = passgen(8)

## Performance

100 000 iterations, 1 core, Core i7 2600k:

length | time (s)
------ | --------
6 | 6.429273437010124
8 | 6.95235215802677
10 | 8.185967321973294
12 | 8.914411939040292
14 | 9.671139033976942
16 | 12.74916506401496
20 | 12.765311673982069

