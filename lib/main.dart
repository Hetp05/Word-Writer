import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Domument #1',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomeEdit(title: 'Domument #1'),
    );
  }
}

class HomeEdit extends StatefulWidget {
  const HomeEdit({Key? key, required this.title}) : super(key: key)

  final String title;

  @override
  State<HomeEdit> createState() => _HomeEditState();
}

class _HomeEditState extends State<HomeEdit> {

  @override
  Widget build(BuildContext context) {
    return CupertinoPageScaffold(
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            
            CupertinoTextFormFieldRow(
              autofocus: true,
              autocorrect: true,
              maxLines: 47,
              obscureText: false,
            )

          ],
        ),
      ),
    );
  }
}
