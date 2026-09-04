// React Theme — extracted from https://veloura-hotel-template.webflow.io
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '48': string;
    '56': string;
    '64': string;
    '96': string;
    '128': string;
    '217.6': string;
    '115.2': string;
    '76.8': string;
    '54.4': string;
    '51.2': string;
    '36.8': string;
    '30.4': string;
 *   };
 *   space: {
    '1': string;
    '32': string;
    '38': string;
    '48': string;
    '77': string;
    '90': string;
    '102': string;
    '112': string;
    '128': string;
    '136': string;
    '160': string;
    '240': string;
    '320': string;
    '448': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#9e4632",
    "secondary": "#471b10",
    "accent": "#ba5d48",
    "background": "#2a0800",
    "foreground": "#000000",
    "neutral50": "#f3eeed",
    "neutral100": "#000000",
    "neutral200": "#ffffff"
  },
  "fonts": {
    "body": "'Funnel Display', sans-serif"
  },
  "fontSizes": {
    "48": "48px",
    "56": "56px",
    "64": "64px",
    "96": "96px",
    "128": "128px",
    "217.6": "217.6px",
    "115.2": "115.2px",
    "76.8": "76.8px",
    "54.4": "54.4px",
    "51.2": "51.2px",
    "36.8": "36.8px",
    "30.4": "30.4px"
  },
  "space": {
    "1": "1px",
    "32": "32px",
    "38": "38px",
    "48": "48px",
    "77": "77px",
    "90": "90px",
    "102": "102px",
    "112": "112px",
    "128": "128px",
    "136": "136px",
    "160": "160px",
    "240": "240px",
    "320": "320px",
    "448": "448px"
  },
  "radii": {
    "md": "10px",
    "lg": "14px",
    "xl": "20px",
    "full": "999px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#9e4632",
      "light": "hsl(11, 52%, 56%)",
      "dark": "hsl(11, 52%, 26%)"
    },
    "secondary": {
      "main": "#471b10",
      "light": "hsl(12, 63%, 32%)",
      "dark": "hsl(12, 63%, 10%)"
    },
    "background": {
      "default": "#2a0800",
      "paper": "#703324"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#2a0800"
    }
  },
  "typography": {
    "fontFamily": "'Funnel Sans', sans-serif",
    "h1": {
      "fontSize": "64px",
      "fontWeight": "500",
      "lineHeight": "76.8px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": []
};

export default theme;
