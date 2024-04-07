import { Component, OnInit } from '@angular/core';
import Typed from 'typed.js';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    // Initialize Typed.js
    const typed = new Typed(".auto-type", {
      strings: ["Image Haven", "Online Album", "Best of World's Images"],
      typeSpeed: 150,
      backSpeed: 50,
      loop: true
    });
  }

}
