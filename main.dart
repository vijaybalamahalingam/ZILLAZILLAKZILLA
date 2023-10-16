import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String _title = 'Title';
  String _body = 'Body';

  void _getRandomText() async {
    final response =
        await http.get(Uri.parse('https://jsonplaceholder.typicode.com/posts'));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final randomIndex = DateTime.now().millisecondsSinceEpoch % data.length;
      setState(() {
        _title = data[randomIndex]['title'];
        _body = data[randomIndex]['body'];
      });
    } else {
      throw Exception('Failed to load text');
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Aster App',
      home: Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
          backgroundColor: Colors.black,
          title: const Text('Aster App',
              style: TextStyle(fontWeight: FontWeight.w400),
              textAlign: TextAlign.center),
          flexibleSpace: Container(
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                gradient: const LinearGradient(colors: [
                  Color.fromARGB(255, 50, 50, 50),
                  Color.fromARGB(0, 31, 18, 18)
                ], begin: Alignment.bottomLeft, end: Alignment.topRight)),
          ),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(8.0, 0.0, 8.0, 50),
                  child: Container(
                    height: 350,
                    width: 350,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      gradient: const LinearGradient(
                        colors: [
                          Color.fromARGB(255, 50, 50, 50),
                          Color.fromARGB(0, 31, 18, 18),
                        ],
                        begin: Alignment.bottomLeft,
                        end: Alignment.topRight,
                      ),
                    ),
                    child: Center(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            textAlign: TextAlign.center,
                            _title,
                            style: const TextStyle(
                                fontWeight: FontWeight.w300,
                                fontSize: 30,
                                color: Colors.white),
                          ),
                          const SizedBox(height: 30),
                          Text(
                            style: const TextStyle(
                                fontWeight: FontWeight.w200,
                                fontSize: 20,
                                color: Colors.white),
                            _body,
                            textAlign: TextAlign.center,
                          ),
                          const SizedBox(height: 20),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
            Container(
              decoration: const BoxDecoration(
                  gradient:
                      RadialGradient(colors: [Colors.white, Colors.black12])),
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                    minimumSize: const Size(60, 50),
                    shape: const StadiumBorder(),
                    backgroundColor: const Color.fromARGB(255, 31, 31, 31)),
                // style: ElevatedButton.styleFrom(
                //  backgroundColor: Colors.deepPurple),
                onPressed: _getRandomText,
                child: const Text('Get Random Data',
                    style:
                        TextStyle(fontSize: 20, fontWeight: FontWeight.w300)),
              ),
            )
          ],
        ),
      ),
    );
  }
}
