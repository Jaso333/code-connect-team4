import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserData } from './user-form/user-form.component';

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  private apiUrl = 'http://localhost:55555/users'; // Replace with your API URL

  constructor(private http: HttpClient) { }

  getUsers(): Observable<UserData[]> {
    return this.http.get<UserData[]>(this.apiUrl);
  }

  getUserById(id: number): Observable<UserData> {
    return this.http.get<UserData>(`${this.apiUrl}/${id}`);
  }

  createUser(user: UserData): Observable<UserData> {
    return this.http.post<UserData>(this.apiUrl, user);
  }

  updateUser(username: string, user: UserData): Observable<UserData> {
    return this.http.put<UserData>(`${this.apiUrl}/${username}`, user);
  }

  deleteUser(username: string): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${username}`);
  }
}
