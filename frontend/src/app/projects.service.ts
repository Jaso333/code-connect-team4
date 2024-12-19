import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProjectsService {
  private apiUrl = 'http://localhost:55555/projects'; // Replace with your API URL

  constructor(private http: HttpClient) { }

  getProjects(): Observable<ProjectData[]> {
    return this.http.get<ProjectData[]>(this.apiUrl);
  }

  getProjectById(id: number): Observable<ProjectData> {
    return this.http.get<ProjectData>(`${this.apiUrl}/${id}`);
  }

  createProject(project: ProjectData): Observable<ProjectData> {
    return this.http.post<ProjectData>(this.apiUrl, project);
  }

  updateProject(id: number, project: ProjectData): Observable<ProjectData> {
    return this.http.put<ProjectData>(`${this.apiUrl}/${id}`, project);
  }

  deleteProject(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}

export interface ProjectData {
  id: number;
  name: string;
  description: string;
}
