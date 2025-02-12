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
      title: 'Flutter Demo',
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
    _services = fetchServices(); // Fetch data when the screen is initialized
  }

  // Fetch services from Django backend
  Future<List<dynamic>> fetchServices() async {
    final String baseUrl = 'http://127.0.0.1:8000/';
    final response = await http.get(Uri.parse('${baseUrl}service/'));

    if (response.statusCode == 200) {
      return json.decode(response.body); // Decode the response as JSON
    } else {
      throw Exception('Failed to load services');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Services')),
      body: FutureBuilder<List<dynamic>>(
        future: _services,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (snapshot.hasData) {
            final services = snapshot.data!;
            return ListView.builder(
              itemCount: services.length,
              itemBuilder: (context, index) {
                final service = services[index];
                final imageUrl = service['image'] != null
                    ? '${service['image']}' // Fixed URL construction
                    : null;

                return ListTile(
                  title: Text(service['name']),
                  subtitle: Text(service['description'] ?? 'No description'),
                  leading: imageUrl != null
                      ? Image.network(imageUrl) // Display image from URL
                      : Icon(Icons.image_not_supported), // Fallback if no image
                );
              },
            );
          } else {
            return Center(child: Text('No services available'));
          }
        },
      ),
    );
  }
}
