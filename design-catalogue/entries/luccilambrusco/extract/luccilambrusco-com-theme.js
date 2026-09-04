// React Theme — extracted from https://www.luccilambrusco.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '14': string;
    '16': string;
    '28': string;
    '32': string;
    '36': string;
    '48': string;
    '128': string;
 *   };
 *   space: {
    '4': string;
    '20': string;
    '32': string;
    '40': string;
    '60': string;
    '240': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#efecce",
    "secondary": "#b83529",
    "accent": "#dcd69d",
    "background": "#b83529",
    "foreground": "#efecce"
  },
  "fonts": {
    "body": "'Flatface Script', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "14": "14px",
    "16": "16px",
    "28": "28px",
    "32": "32px",
    "36": "36px",
    "48": "48px",
    "128": "128px"
  },
  "space": {
    "4": "4px",
    "20": "20px",
    "32": "32px",
    "40": "40px",
    "60": "60px",
    "240": "240px"
  },
  "radii": {
    "md": "10px",
    "xl": "20px",
    "full": "50px"
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
      "main": "#efecce",
      "light": "hsl(55, 51%, 95%)",
      "dark": "hsl(55, 51%, 72%)"
    },
    "secondary": {
      "main": "#b83529",
      "light": "hsl(5, 64%, 59%)",
      "dark": "hsl(5, 64%, 29%)"
    },
    "background": {
      "default": "#b83529",
      "paper": "#efecce"
    },
    "text": {
      "primary": "#efecce",
      "secondary": "#b83529"
    }
  },
  "typography": {
    "fontFamily": "'ABC Solar', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "48px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "700",
      "lineHeight": "25.2px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "20px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": []
};

export default theme;
