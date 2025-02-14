import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Флаттер Демо',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ServiceScreen(),
    );
  }
}

class ServiceScreen extends StatefulWidget {
  @override
  _ServiceScreenState createState() => _ServiceScreenState();
}

class _ServiceScreenState extends State<ServiceScreen> {
  late Future<List<dynamic>> _services;

  @override
  void initState() {
    super.initState();
    _services = fetchServices(); // Дэлгэц нээгдэхэд мэдээлэл татах
  }

  // Django серверээс үйлчилгээ татах функц
  Future<List<dynamic>> fetchServices() async {
    final String baseUrl = 'http://127.0.0.1:8000/';
    final response = await http.get(Uri.parse('${baseUrl}service/'));

    if (response.statusCode == 200) {
      return json.decode(
          utf8.decode(response.bodyBytes)); // UTF-8 кодчилолтой JSON хөрвүүлэх
    } else {
      throw Exception('Үйлчилгээг татаж чадсангүй');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Үйлчилгээ')),
      body: FutureBuilder<List<dynamic>>(
        future: _services,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Алдаа: ${snapshot.error}'));
          } else if (snapshot.hasData) {
            final services = snapshot.data!;
            return ListView.builder(
              itemCount: services.length,
              itemBuilder: (context, index) {
                final service = services[index];
                final imageUrl = service['image'] != null
                    ? '${service['image']}' // URL-ийг засварласан
                    : null;

                return ListTile(
                  title: Text(service['name'],
                      style: TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text(service['description'] ?? 'Тайлбар алга'),
                  leading: imageUrl != null
                      ? Image.network(imageUrl,
                          width: 50,
                          height: 50,
                          fit: BoxFit.cover) // Зураг харуулах
                      : Icon(Icons.image_not_supported), // Зураг байхгүй үед
                );
              },
            );
          } else {
            return Center(child: Text('Ямар ч үйлчилгээ байхгүй'));
          }
        },
      ),
    );
  }
}
