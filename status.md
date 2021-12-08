# Whats missing

ODW-TakeHome

→ Insert.html exists
  GET https://proxy/insert.html [200 OK, 579B, 50ms]
  ✓  HTTP response code 200 received
  ✓  Checksum validation

→ Select.html exist
  GET https://proxy/select.html [200 OK, 1.11kB, 3ms]
  ✓  HTTP response code 200 received
  ✓  Checksum validation

→ Insert person
  POST https://proxy/person [500 INTERNAL SERVER ERROR, 473B, 14ms]
  1. HTTP response code 200 received

→ Select person
  GET https://proxy/persons [500 INTERNAL SERVER ERROR, 473B, 7ms]
  2. HTTP response code 200 received
  3. Check selectPersons
  4. Test inserted values

┌─────────────────────────┬──────────────────┬──────────────────┐
│                         │         executed │           failed │
├─────────────────────────┼──────────────────┼──────────────────┤
│              iterations │                1 │                0 │
├─────────────────────────┼──────────────────┼──────────────────┤
│                requests │                4 │                0 │
├─────────────────────────┼──────────────────┼──────────────────┤
│            test-scripts │                8 │                0 │
├─────────────────────────┼──────────────────┼──────────────────┤
│      prerequest-scripts │                5 │                0 │
├─────────────────────────┼──────────────────┼──────────────────┤
│              assertions │                8 │                4 │
├─────────────────────────┴──────────────────┴──────────────────┤
│ total run duration: 204ms                                     │
├───────────────────────────────────────────────────────────────┤
│ total data received: 1.8kB (approx)                           │
├───────────────────────────────────────────────────────────────┤
│ average response time: 18ms [min: 3ms, max: 50ms, s.d.: 18ms] │
└───────────────────────────────────────────────────────────────┘

  #  failure         detail                                                  
                                                                             
 1.  AssertionError  HTTP response code 200 received                         
                     expected response to have status code 200 but got 500   
                     at assertion:0 in test-script                           
                     inside "Insert person"                                  
                                                                             
 2.  AssertionError  HTTP response code 200 received                         
                     expected response to have status code 200 but got 500   
                     at assertion:0 in test-script                           
                     inside "Select person"                                  
                                                                             
 3.  JSONError       Check selectPersons                                     
                     Unexpected token '<' at 1:1                             
                     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"> 
                     ^                                                       
                     at assertion:1 in test-script                           
                     inside "Select person"                                  
                                                                             
 4.  JSONError       Test inserted values                                    
                     Unexpected token '<' at 1:1                             
                     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"> 
                     ^                                                       
                     at assertion:2 in test-script                           
                     inside "Select person"    

# Remember to change!
* backend host to database!
* update certs to match site.crt, site.key og rootCA.pem