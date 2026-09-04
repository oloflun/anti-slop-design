// React Theme — extracted from https://www.raus.life/
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
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '22': string;
    '28': string;
    '36': string;
    '40': string;
    '84': string;
 *   };
 *   space: {
    '2': string;
    '32': string;
    '40': string;
    '48': string;
    '53': string;
    '80': string;
    '96': string;
    '120': string;
    '192': string;
    '211': string;
 *   };
 *   radii: {
    sm: string;
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
    "primary": "#23212c",
    "secondary": "#dd5000",
    "accent": "#a6dfff",
    "background": "#fdf9ed",
    "foreground": "#23212c",
    "neutral50": "#ffffff",
    "neutral100": "#fdf9ed",
    "neutral200": "#000000"
  },
  "fonts": {
    "body": "'fonts', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "22": "22px",
    "28": "28px",
    "36": "36px",
    "40": "40px",
    "84": "84px"
  },
  "space": {
    "2": "2px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "53": "53px",
    "80": "80px",
    "96": "96px",
    "120": "120px",
    "192": "192px",
    "211": "211px"
  },
  "radii": {
    "sm": "4px",
    "lg": "16px",
    "xl": "20px",
    "full": "99px"
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
      "main": "#23212c",
      "light": "hsl(251, 14%, 30%)",
      "dark": "hsl(251, 14%, 10%)"
    },
    "secondary": {
      "main": "#dd5000",
      "light": "hsl(22, 100%, 58%)",
      "dark": "hsl(22, 100%, 28%)"
    },
    "background": {
      "default": "#fdf9ed",
      "paper": "#000000"
    },
    "text": {
      "primary": "#23212c",
      "secondary": "#dd5000"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "300",
      "lineHeight": "36px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "300",
      "lineHeight": "30px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "400",
      "lineHeight": "26px"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "400",
      "lineHeight": "22px"
    }
  },
  "shape": {
    "borderRadius": 4
  },
  "shadows": []
};

export default theme;
